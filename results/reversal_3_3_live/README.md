# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 10:10:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           93.75               16            0.97              0.72        106.41                21.58         0.543            pass              0.525             21.4                           0.216                1.63              0.030                                 ok            True                  False
  CSCO           81.82               22            1.42              1.09        108.99                36.36         0.542            pass              0.231             16.2                           0.188               -1.54             -0.165                                 ok            True                  False
  REGN          100.00               26            0.86              5.12        849.83                27.66         0.516            pass              0.615             18.8                           0.163                2.19              0.060                                 ok            True                  False
  MRVL           81.58               38            0.62              0.89        206.10                78.54         0.627            pass              0.520             76.3                           0.594              -18.25             -1.996 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00               33            0.62              0.24         54.57                55.99         0.604            pass              0.630              5.4                           0.051              -12.79             -1.931 downtrend_blocked_slope_and_streak           False                  False
  MCHP           86.96               23            2.41              1.22         72.24                58.99         0.538            pass              0.399             24.2                           0.152               -5.77             -0.530            downtrend_blocked_slope           False                  False
  FAST          100.00               27            0.08              0.03         47.92                20.75         0.527            pass              0.830             87.9                           0.437               -5.47             -0.699 downtrend_blocked_slope_and_streak           False                  False
  SNPS           92.00               50            0.08              0.23        415.87                57.94         0.526            pass              0.837             88.0                           0.443                4.45              0.698                                 ok           False                  False
 CMCSA           92.86               28            0.47              0.09         26.77                26.14         0.518            pass              0.612             32.4                           0.238                1.00             -0.071                                 ok           False                  False
  AMGN           96.77               31            0.24              0.74        442.52                21.97         0.501            pass              0.823             77.7                           0.530                2.45              0.036                                 ok           False                  False
  DRAM           83.33               30            2.70              1.06         55.76                63.42         0.500 below_threshold              0.336             21.3                           0.264               -5.01             -0.276            downtrend_blocked_slope           False                  False
  CHTR           86.67               15            3.32              3.69        157.39                59.56         0.498 below_threshold              0.295             11.4                           0.167                4.02              0.277                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-03T10:10:01.856721-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:05:01.913040-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:00:03.820107-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "MSTR261009C00122000", "fill_price": 16.575, "pnl": 10200.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 44.44, "ticker": "MSTR"}
2026-09-03T09:50:05.699524-04:00      manage_1000               exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CPRT261016C00032500", "fill_price": 2.8, "pnl": 16560.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 69.7, "ticker": "CPRT"}
2026-09-03T00:00:02.675455-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-09-02T15:10:01.537083-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:05:01.526637-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T14:58:03.772540-04:00       entry_1500              entry {"allocated_cash": 22950.0, "asset_type": "option", "contract_symbol": "MSTR261009C00122000", "contracts": 20, "early_entry_score": 0.304, "entry_mode": "regular", "entry_option_price": 11.475, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 141.0, "option_spread_pct": 6.54, "option_volume": 20.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.589}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903101001)

</details>
