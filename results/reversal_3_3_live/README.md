# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-09 15:45:05 EDT`
Last processed slot: `manual`

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

- Cash: `$58,874.30`
- Equity: `$114,874.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$-2,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   0    160     58400.0                 56000.0         3.65            3.5       59.31         59.04          bid_ask_mid                        3.5                bid_ask_mid                    True         -2400.0                  -4.11          93.1               29              1.17         50.42           49.95                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261120C00115000     74          2026-10-08         2026-10-09         7.25       8.425 8695.0   16.206897 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           91.30               23            1.55              0.65         59.73                46.57         0.529            pass              0.450              3.1                           0.076                3.05              0.302                                 ok            True                  False
  INTU           87.88               33            0.79              1.67        303.16                43.01         0.510            pass              0.525             36.8                           0.259                9.83              1.260                                 ok            True                  False
  SOXL           86.21               29            2.61              2.60        141.41               115.52         0.616            pass              0.422             22.8                           0.267               -8.35              0.074           downtrend_blocked_streak           False                  False
  META           84.21               38            0.20              1.02        720.45                52.31         0.579            pass              0.563             68.8                           0.519               -4.29             -0.184           downtrend_blocked_streak           False                  False
  QCOM           92.68               41            0.27              0.34        175.87                56.70         0.550            pass              0.859             88.6                           0.707              -13.09             -1.009 downtrend_blocked_slope_and_streak           False                  False
  NFLX           70.59               17            1.52              0.76         71.24                35.32         0.541            pass              0.144             14.6                           0.281               -0.93              0.027                                 ok           False                  False
  PAYX           80.56               36            0.41              0.30        104.33                40.01         0.533            pass              0.248              2.3                           0.242                2.62              0.399                                 ok           False                  False
  MDLZ           96.00               25            0.27              0.12         60.62                17.90         0.529            pass              0.772             72.9                           0.529                1.31              0.215                                 ok           False                  False
  INTC           83.33               24            2.58              1.93        106.25                69.62         0.521            pass              0.265             10.4                           0.195              -15.19             -1.258 downtrend_blocked_slope_and_streak           False                  False
  AMAT           84.21               38            0.48              1.71        508.84                47.71         0.502            pass              0.496             48.8                           0.349                4.56              0.503                                 ok           False                  False
  LRCX           81.58               38            0.64              1.45        319.97                52.42         0.491 below_threshold              0.442             54.7                           0.300                1.05              0.209                                 ok           False                  False
 CMCSA          100.00                3            2.62              0.39         21.04                20.06         0.487 below_threshold              0.521             24.0                           0.466               -4.26             -0.305            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-09T15:10:06.439526-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T15:05:05.713362-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T15:00:05.326710-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T14:55:05.363044-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-09T14:50:06.079199-04:00       entry_1500              entry {"allocated_cash": 58400.0, "asset_type": "option", "contract_symbol": "CTSH261120C00060000", "contracts": 160, "early_entry_score": 0.592, "entry_mode": "regular", "entry_option_price": 3.65, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 209.0, "option_spread_pct": 8.22, "option_volume": 38.0, "success_rate": 93.1, "ticker": "CTSH", "timing_score": 0.518}
2026-10-09T14:50:06.079199-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-09", "training_samples": 5994, "window": 5}
2026-10-09T13:50:04.651779-04:00      manage_1400               exit                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 8.425, "pnl": 8695.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.21, "ticker": "CSCO"}
2026-10-09T11:44:59.466753-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-09T00:00:06.171329-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-08T15:10:05.020875-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261009154505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261009154505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261009154505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261009154505)

</details>
