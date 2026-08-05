# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 15:05:03 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$16,083.25`
- Equity: `$31,840.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-08-05                   0     55     15757.5                 15757.5         2.86           2.86       58.15         58.08          bid_ask_mid                       2.86                bid_ask_mid                    True             0.0                    0.0         91.18               34              0.66         31.86           32.37                  60.15                7033.0           38.0               0.04                      ok
```

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.44               36            0.53              0.26         70.15                58.11         0.622            pass              0.715             31.5                           0.399               13.87              1.705                       ok            True                  False
  PYPL           90.91               33            0.78              0.32         58.40                60.15         0.612            pass              0.726             73.6                           0.447                4.63              0.476                       ok            True                  False
  PAYX          100.00               17            0.73              0.61        118.40                35.13         0.583            pass              0.734             76.2                           0.585                7.47              0.765                       ok            True                  False
  CTAS           90.00               20            1.36              1.94        202.82                37.77         0.580            pass              0.481             29.9                           0.426               -0.24             -0.120                       ok            True                  False
  MRVL           80.00               35            1.80              2.76        217.41               100.52         0.579            pass              0.377             50.7                           0.361                1.73              0.259                       ok            True                  False
  MSFT           81.58               38            0.55              1.89        492.00                57.86         0.550            pass              0.470             62.1                           0.564               25.56              3.080                       ok            True                  False
   PEP           84.00               25            0.59              0.57        138.85                25.68         0.546            pass              0.353             30.5                           0.262                1.94              0.236                       ok            True                  False
  CPRT           85.00               20            1.96              0.40         29.23                38.86         0.500 below_threshold              0.343             31.1                           0.475                6.09              0.611                       ok            True                  False
  SOXL           80.00               35            2.19              2.15        138.98               182.46         0.769            pass              0.451             69.0                           0.685              -15.00             -1.762 downtrend_blocked_streak           False                  False
   WDC           83.87               31            0.82              3.15        547.21                99.34         0.701            pass              0.453             46.4                           0.337               -2.27              0.161 downtrend_blocked_streak           False                  False
  AMAT           90.91               33            0.99              3.79        544.99                87.24         0.659            pass              0.709             66.2                           0.498               -2.30             -0.291 downtrend_blocked_streak           False                  False
  TMUS           85.71                7            2.65              3.29        175.80                55.59         0.637            pass              0.283             22.2                           0.307               -9.65             -0.458  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-05T15:05:03.750105-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T15:00:02.739208-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:55:01.792293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-05T14:50:06.241655-04:00       entry_1500                   entry {"allocated_cash": 15757.5, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 55, "early_entry_score": 0.753, "entry_mode": "regular", "entry_option_price": 2.865, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7033.0, "option_spread_pct": 3.84, "option_volume": 38.0, "success_rate": 91.18, "ticker": "PYPL", "timing_score": 0.614}
2026-08-05T14:50:06.241655-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                             {"early_entry_score": 0.655, "option_liquidity_status": "low_volume", "option_open_interest": 2148.0, "option_spread_pct": 6.06, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "GEHC", "timing_score": 0.628}
2026-08-05T14:50:06.241655-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-05", "training_samples": 5567, "window": 5}
2026-08-05T12:00:04.693066-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200                    exit                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805150503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805150503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805150503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805150503)

</details>
