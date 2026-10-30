# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 10:05:02 EDT`
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

- Cash: `$117,176.55`
- Equity: `$117,176.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  MSTR     option         option MSTR261218C00140000     41          2026-10-29         2026-10-30       15.025     13.5225 -6160.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           91.30               23            2.32              4.02        246.10                59.82         0.520          pass              0.488             16.0                           0.175               16.73              2.038                                 ok            True                  False
  SBUX           86.67               15            1.61              1.19        105.00                26.25         0.518          pass              0.310             15.8                           0.152                6.45              0.739                                 ok            True                  False
  PANW           80.49               41            0.59              1.56        379.90                58.77         0.506          pass              0.484             73.5                           0.432               10.63              1.550                                 ok            True                  False
  NXPI           92.31               13            2.32              4.33        264.15                41.25         0.504          pass              0.434             11.7                           0.188               13.30              1.362                                 ok            True                  False
  MSFT          100.00               16            1.41              5.22        527.90                19.58         0.502          pass              0.648             52.8                           0.690               -1.20             -0.068                                 ok            True                  False
  AAPL           94.12               17            1.13              2.77        347.72                13.86         0.500          pass              0.617             47.8                           0.373                0.44              0.122                                 ok            True                  False
  FTNT           90.00               40            0.79              0.77        138.77                91.61         0.643          pass              0.752             73.6                           0.697              -18.41             -1.472            downtrend_blocked_slope           False                  False
 GOOGL           77.78               27            1.00              1.99        282.97                51.94         0.614          pass              0.298             41.1                           0.510              -17.50             -1.802 downtrend_blocked_slope_and_streak           False                  False
  GOOG           78.57               28            0.96              1.89        281.51                50.42         0.604          pass              0.308             42.6                           0.413              -17.00             -1.743 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               18            2.41              3.44        202.63                50.04         0.548          pass              0.614             35.2                           0.370               -4.16             -0.439            downtrend_blocked_slope           False                  False
   CSX           70.00               10            1.41              0.51         52.02                27.59         0.544          pass              0.115             20.2                           0.215                5.80              0.920                                 ok           False                  False
  MELI           70.83               24            1.81             21.02       1651.12                48.11         0.533          pass              0.267             40.1                           0.541              -11.12             -1.487 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-30T10:05:02.865531-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:00:06.058650-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T09:50:05.911217-04:00      manage_1000               exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MSTR261218C00140000", "fill_price": 13.5225, "pnl": -6160.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-10-30T00:00:05.693119-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 91, 'empty': 2}
2026-10-29T15:10:05.741220-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-29T15:05:04.728633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-29T15:00:04.604775-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-29T14:55:06.721591-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-29T14:50:05.643869-04:00       entry_1500              entry {"allocated_cash": 61602.5, "asset_type": "option", "contract_symbol": "MSTR261218C00140000", "contracts": 41, "early_entry_score": 0.432, "entry_mode": "regular", "entry_option_price": 15.025, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1665.0, "option_spread_pct": 2.33, "option_volume": 96.0, "success_rate": 86.96, "ticker": "MSTR", "timing_score": 0.554}
2026-10-29T14:50:05.643869-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-29", "training_samples": 6227, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030100502)

</details>
