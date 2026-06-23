# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-23 10:17:41 EDT`
Last processed slot: `early_entry_1015`

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
  AVGO           87.88               33            0.80              2.20        391.19                76.66         0.641            pass              0.685             85.7                           0.845               -1.77              0.219                                 ok            True                  False
  INTC           92.31               26            2.47              2.44        139.89                94.51         0.588            pass              0.713             73.2                           0.910               24.65              2.591                                 ok            True                  False
  UPRO           94.12               17            2.24              2.22        140.47                49.83         0.557            pass              0.640             53.7                           0.787               -0.23              0.390                                 ok            True                  False
  MRVL          100.00                9            5.93             12.78        302.38               151.43         0.696            pass              0.597             42.6                           0.813                0.26              1.148                                 ok           False                  False
   HON           61.54               13            1.41              2.24        227.15                40.60         0.565            pass              0.208             43.8                           0.638                6.19              0.881                                 ok           False                  False
  CSCO           86.67               15            1.80              1.53        120.87                40.78         0.563            pass              0.398             43.4                           0.615               -3.87             -0.207           downtrend_blocked_streak           False                  False
  SHOP           84.09               44            0.11              0.08        107.94                55.98         0.527            pass              0.633             90.4                           0.438               -2.64             -0.185                                 ok           False                  False
  INTU           76.19               42            0.43              0.78        257.44                62.45         0.517            pass              0.395             47.6                           0.319              -15.99             -1.476 downtrend_blocked_slope_and_streak           False                  False
  FAST           92.00               25            0.89              0.29         46.00                23.77         0.498 below_threshold              0.597             42.3                           0.575               -0.63             -0.144                                 ok           False                  False
  ROST           87.50                8            1.95              3.23        235.58                39.21         0.492 below_threshold              0.463             71.2                           0.437                2.37              0.167                                 ok           False                  False
   KDP          100.00                3            3.01              0.65         30.59                21.52         0.491 below_threshold              0.481             10.5                           0.243               -2.63             -0.286            downtrend_blocked_slope           False                  False
  ODFL           91.89               37            0.42              0.65        219.24                45.20         0.486 below_threshold              0.822             92.2                           0.502              -11.51             -1.471 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T00:00:04.979813-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-22T15:10:01.120080-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:00:02.230019-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:55:01.213018-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:50:05.502859-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-22", "training_samples": 5273, "window": 5}
2026-06-22T14:50:05.502859-04:00       entry_1500              entry {"allocated_cash": 10500.0, "asset_type": "option", "contract_symbol": "MRVL260724C00310000", "contracts": 3, "early_entry_score": 0.746, "entry_mode": "regular", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 195.0, "option_spread_pct": 5.71, "option_volume": 52.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.836}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260623101741)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260623101741)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260623101741)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260623101741)

</details>
