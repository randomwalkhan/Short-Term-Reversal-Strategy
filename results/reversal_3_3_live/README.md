# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:00:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$75,459.30`
- Equity: `$135,444.30`
- Realized PnL: `$123,274.30`
- Unrealized PnL: `$2,170.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00290000       2026-10-12                   1     31     57815.0                 59985.0        18.65          19.35      291.07        291.27          bid_ask_mid                      19.35                bid_ask_mid                    True          2170.0                   3.75         83.33               12              2.35         48.77           52.52                  62.49                 920.0          121.0               0.05                      ok
```

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0    27.39726 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           96.00               25            0.55              0.13         32.70                30.00         0.545          pass              0.647             30.8                           0.213                4.96              0.634                                 ok            True                  False
   CEG           85.29               34            0.57              1.18        293.38                56.17         0.540          pass              0.586             77.0                           0.759               10.44              1.653                                 ok            True                  False
   EXC           83.33               18            0.81              0.24         42.02                16.28         0.502          pass              0.192              0.0                           0.150                2.78              0.421                                 ok            True                  False
  INTC           88.57               35            1.11              0.79        101.01                67.41         0.572          pass              0.644             64.0                           0.791              -13.55             -1.876 downtrend_blocked_slope_and_streak           False                  False
  MPWR           87.50               24            1.41             13.01       1313.65                51.39         0.555          pass              0.490             46.9                           0.406               -3.94             -0.333            downtrend_blocked_slope           False                  False
  MDLZ           95.45               22            0.44              0.19         61.71                19.83         0.538          pass              0.555              6.9                           0.094                4.63              0.659                                 ok           False                  False
   XEL           76.92               13            0.90              0.47         73.97                18.13         0.532          pass              0.073              0.0                           0.150                3.98              0.546                                 ok           False                  False
   PEP           76.19               21            0.47              0.41        126.50                21.61         0.515          pass              0.125              0.0                           0.150               -2.02             -0.065                                 ok           False                  False
  UPRO           83.78               37            0.11              0.12        155.41                28.94         0.512          pass              0.578             82.0                           0.579                4.95              0.602                                 ok           False                  False
  CSCO           94.29               35            0.16              0.13        115.29                34.19         0.508          pass              0.877             93.0                           0.899                8.10              0.941                                 ok           False                  False
  CDNS           78.95               19            1.54              3.76        346.81                33.13         0.508          pass              0.173             20.6                           0.352                5.82              0.463                                 ok           False                  False
  SHOP           85.71               42            0.33              0.42        179.04                48.43         0.506          pass              0.670             89.0                           0.933               20.48              2.092                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-13T10:00:05.694425-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T09:50:04.590337-04:00      manage_1000               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "CTSH261120C00060000", "fill_price": 4.65, "pnl": 16000.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 27.4, "ticker": "CTSH"}
2026-10-13T00:00:05.318337-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-10-12T15:10:05.555878-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T15:05:06.325460-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T15:00:05.898503-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T14:55:06.164837-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-12T14:50:02.373216-04:00       entry_1500              entry {"allocated_cash": 57815.0, "asset_type": "option", "contract_symbol": "CEG261120C00290000", "contracts": 31, "early_entry_score": 0.18, "entry_mode": "regular", "entry_option_price": 18.65, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 920.0, "option_spread_pct": 4.83, "option_volume": 121.0, "success_rate": 83.33, "ticker": "CEG", "timing_score": 0.545}
2026-10-12T14:50:02.373216-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-12", "training_samples": 6005, "window": 5}
2026-10-12T12:00:04.227731-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013100005)

</details>
