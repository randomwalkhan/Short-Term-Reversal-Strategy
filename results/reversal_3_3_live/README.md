# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 14:30:05 EDT`
Last processed slot: `manage_1430`

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
  ROST           94.12               17            1.30              2.19        239.19                38.75         0.599          pass              0.564             27.0                           0.349                5.98              0.616                                 ok            True                  False
  CPRT           86.67               15            1.71              0.37         30.59                31.00         0.542          pass              0.289              7.9                           0.275               -6.48             -0.209                                 ok            True                  False
   BKR           81.25               32            0.89              0.39         62.97                39.91         0.516          pass              0.433             67.0                           0.710               -0.62             -0.204                                 ok            True                  False
  AMGN           92.31               26            0.60              1.49        354.56                28.14         0.514          pass              0.644             52.5                           0.393                7.27              0.670                                 ok            True                  False
  CTAS           95.83               24            1.13              1.40        175.68                29.28         0.509          pass              0.636             30.6                           0.245                0.80              0.233                                 ok            True                  False
   KHC          100.00                3            1.25              0.21         24.30                26.17         0.658          pass              0.480              4.7                           0.215                3.77              0.774                                 ok           False                  False
   TRI           81.48               27            0.39              0.22         81.32                63.37         0.653          pass              0.375             52.3                           0.246              -13.69             -1.142 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.65               23            1.18              1.87        225.41                32.50         0.555          pass              0.629             29.0                           0.177               -4.37             -0.301            downtrend_blocked_slope           False                  False
  WDAY           84.85               33            1.29              1.18        130.29                70.45         0.553          pass              0.346              2.8                           0.092              -17.88             -1.902 downtrend_blocked_slope_and_streak           False                  False
  KLAC           92.11               38            0.29              0.52        254.32                77.77         0.542          pass              0.799             78.4                           0.590               30.82              2.390                                 ok           False                  False
   WMT           87.10               31            0.46              0.39        120.87                34.65         0.542          pass              0.615             77.2                           0.559                5.13              0.578                                 ok           False                  False
 CMCSA           66.67                9            1.76              0.30         24.37                24.55         0.530          pass              0.053              0.0                           0.114               -3.91             -0.147                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615143005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615143005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615143005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615143005)

</details>
