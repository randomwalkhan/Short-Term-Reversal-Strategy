# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 13:50:01 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$27,308.25`
- Equity: `$27,308.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           94.12               17            1.27              2.14        239.21                38.75         0.601          pass              0.569             28.7                           0.336                6.01              0.618                                 ok            True                  False
   BKR           80.77               26            1.05              0.46         62.94                39.91         0.547          pass              0.365             61.1                           0.506               -0.78             -0.212                                 ok            True                  False
  CPRT           86.67               15            1.71              0.37         30.59                31.00         0.543          pass              0.279              4.5                           0.203               -6.48             -0.209                                 ok            True                  False
  KLAC           90.62               32            0.91              1.62        253.84                77.77         0.537          pass              0.581             32.4                           0.234               30.01              2.361                                 ok            True                  False
  AMGN           91.67               24            0.70              1.75        354.45                28.14         0.520          pass              0.589             44.2                           0.229                7.16              0.665                                 ok            True                  False
  DXCM           81.82               22            1.71              0.90         74.98                46.69         0.517          pass              0.270             29.8                           0.412               -1.06              0.219                                 ok            True                  False
  CTAS           96.30               27            0.94              1.16        175.78                29.28         0.501          pass              0.691             42.5                           0.337                1.00              0.242                                 ok            True                  False
   KHC          100.00                3            1.12              0.19         24.31                26.17         0.667          pass              0.485              6.2                           0.209                3.91              0.780                                 ok           False                  False
  WDAY           88.37               43            0.18              0.16        130.73                70.45         0.567          pass              0.739             86.4                           0.407              -16.96             -1.851 downtrend_blocked_slope_and_streak           False                  False
  CSCO           93.75               32            0.47              0.40        120.93                43.07         0.554          pass              0.761             64.0                           0.677               -0.66             -0.497                                 ok           False                  False
 CMCSA           75.00               12            1.57              0.27         24.38                24.55         0.532          pass              0.082              5.0                           0.082               -3.73             -0.138                                 ok           False                  False
   WMT           89.47               38            0.20              0.17        120.97                34.65         0.513          pass              0.761             90.1                           0.565                5.41              0.590                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                  detail
2026-06-12T15:10:11.830500-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T15:05:11.809096-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:50:07.527766-04:00   entry_1500           entry_skipped                                                                                                                                                            {"budget": 13654.13, "entry_cost": 15345.0, "reason": "insufficient_cash", "ticker": "ASML"}
2026-06-12T14:50:07.527766-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.73, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 0.0, "option_spread_pct": 7.0, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.565}
2026-06-12T14:50:07.527766-04:00   entry_1500          timing_overlay                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-12", "training_samples": 5261, "window": 5}
2026-06-12T13:30:06.922165-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                           {'saved': 93}
2026-06-11T16:00:02.840701-04:00  manage_1600                    exit                                                                       {"asset_type": "option", "contract_symbol": "PAYX260717C00100000", "fill_price": 4.725, "pnl": -1417.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-06-11T15:10:05.901456-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615135001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615135001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615135001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615135001)

</details>
