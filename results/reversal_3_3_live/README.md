# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-23 09:35:06 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   WMT     option         option  WMT260724C00120000     52          2026-06-18         2026-06-23         2.51         3.5  5148.0   39.442231 take_profit_day2_hit_at_scan
  MRVL     option         option MRVL260724C00310000      3          2026-06-22         2026-06-23        35.00        31.5 -1050.0  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AVGO           83.33               18            2.22              6.08        389.52                76.66         0.640            pass              0.388             60.6                           0.800               -3.17              0.154                                 ok            True                  False
  CRWD           88.89               36            0.83              3.91        673.77                62.09         0.558            pass              0.675             69.7                           0.619                1.68              0.369                                 ok            True                   True
  FAST           94.74               19            1.13              0.36         45.96                23.77         0.534            pass              0.506              0.0                           0.206               -0.87             -0.154                                 ok            True                  False
  SBUX           83.33               24            0.70              0.49         99.94                25.68         0.513            pass              0.455             73.8                           0.373                4.88              0.313                                 ok            True                  False
   KDP           94.12               17            1.46              0.31         30.74                21.52         0.509            pass              0.496              7.2                           0.138               -1.07             -0.214                                 ok            True                  False
  MRVL          100.00                3            8.32             17.92        300.18               151.43         0.577            pass              0.516             19.5                           0.603               -2.28              1.031                                 ok           False                  False
   XEL          100.00               26            0.01              0.01         78.81                23.53         0.568            pass              0.855             97.1                           0.521                2.29              0.169                                 ok           False                  False
  PANW           92.86               42            0.17              0.35        286.25                57.24         0.561            pass              0.876             92.4                           0.782                7.35              0.928                                 ok           False                  False
  CSCO           71.43                7            2.76              2.34        120.53                40.78         0.536            pass              0.090             12.1                           0.219               -4.81             -0.252 downtrend_blocked_slope_and_streak           False                  False
   HON           42.86                7            2.31              3.70        226.53                40.60         0.524            pass              0.052              0.0                           0.197                5.21              0.839                                 ok           False                  False
  PCAR           81.25               16            1.59              1.33        119.55                32.72         0.494 below_threshold              0.145              7.5                           0.223               -0.19              0.136                                 ok           False                  False
   LIN           96.77               31            0.33              1.18        516.21                18.72         0.487 below_threshold              0.824             78.6                           0.430                2.61              0.133                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-23T09:35:06.707471-04:00  manage_0930           exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-23T09:35:06.707471-04:00  manage_0930           exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T00:00:04.979813-04:00 data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-22T15:10:01.120080-04:00   entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00   entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:00:02.230019-04:00   entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:55:01.213018-04:00   entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:50:05.502859-04:00   entry_1500          entry {"allocated_cash": 10500.0, "asset_type": "option", "contract_symbol": "MRVL260724C00310000", "contracts": 3, "early_entry_score": 0.746, "entry_mode": "regular", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 195.0, "option_spread_pct": 5.71, "option_volume": 52.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.836}
2026-06-22T14:50:05.502859-04:00   entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-22", "training_samples": 5273, "window": 5}
2026-06-22T03:00:02.560041-04:00 data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260623093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260623093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260623093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260623093506)

</details>
