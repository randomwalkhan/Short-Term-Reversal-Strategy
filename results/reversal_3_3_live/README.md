# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 09:50:05 EDT`
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

- Cash: `$74,478.10`
- Equity: `$74,478.10`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CPRT     option         option CPRT261016C00032500    144          2026-09-01         2026-09-03        1.650       2.800 16560.0   69.696970 take_profit_day2_hit_at_scan
  MSTR     option         option MSTR261009C00122000     20          2026-09-02         2026-09-03       11.475      16.575 10200.0   44.444444 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           83.33               30            1.73              0.68         55.92                63.42         0.557          pass              0.427             49.6                           0.489               -4.06             -0.231                                 ok            True                  False
  AMGN          100.00               19            0.83              2.56        441.74                21.97         0.544          pass              0.584             23.1                           0.309                1.85              0.009                                 ok            True                  False
  CSCO           84.62               26            1.23              0.94        109.05                36.36         0.534          pass              0.335             17.2                           0.168               -1.35             -0.156                                 ok            True                  False
  REGN          100.00               28            0.76              4.55        850.08                27.66         0.509          pass              0.655             28.0                           0.324                2.29              0.065                                 ok            True                  False
  CHTR           90.91               33            1.72              1.91        158.15                59.56         0.508          pass              0.495              0.0                           0.237                5.74              0.352                                 ok            True                  False
  PANW           86.36               44            0.67              1.55        327.82                70.92         0.504          pass              0.626             68.7                           0.487               -6.66             -0.244                                 ok            True                  False
  VRTX           96.88               32            0.81              3.16        555.40                32.13         0.503          pass              0.808             70.3                           0.442                2.22              0.120                                 ok            True                  False
  MNST           88.89               36            0.34              0.10         44.38               424.20         0.999          pass              0.624             37.8                           0.269               -6.78             -0.940 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00               41            0.24              0.09         54.63                55.99         0.582          pass              0.763             35.0                           0.310              -12.46             -1.914 downtrend_blocked_slope_and_streak           False                  False
  MCHP           87.50               24            1.94              0.99         72.34                58.99         0.560          pass              0.466             39.0                           0.240               -5.32             -0.509            downtrend_blocked_slope           False                  False
 CMCSA           93.55               31            0.06              0.01         26.81                26.14         0.528          pass              0.814             86.6                           0.462                1.42             -0.052                                 ok           False                  False
  SBUX           96.30               27            0.41              0.31        106.59                21.58         0.514          pass              0.738             57.6                           0.358                2.20              0.056                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "MSTR261009C00122000", "fill_price": 16.575, "pnl": 10200.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 44.44, "ticker": "MSTR"}
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CPRT261016C00032500", "fill_price": 2.8, "pnl": 16560.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 69.7, "ticker": "CPRT"}
2026-09-03T00:00:02.675455-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-02T15:10:01.537083-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:05:01.526637-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T14:58:03.772540-04:00       entry_1500              entry {"allocated_cash": 22950.0, "asset_type": "option", "contract_symbol": "MSTR261009C00122000", "contracts": 20, "early_entry_score": 0.304, "entry_mode": "regular", "entry_option_price": 11.475, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 141.0, "option_spread_pct": 6.54, "option_volume": 20.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.589}
2026-09-02T14:58:03.772540-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-02", "training_samples": 5758, "window": 5}
2026-09-02T12:00:02.480923-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903095005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903095005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903095005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903095005)

</details>
