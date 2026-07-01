# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 09:57:14 EDT`
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

- Cash: `$14,720.50`
- Equity: `$28,960.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 14240.0         4.58           4.45      126.19        126.18     last_price_stale                        NaN                unavailable                   False          -400.0                  -2.73         93.33               15              1.32         33.41            1.56                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL           95.24               21            3.43              7.15        294.83               157.45         0.672          pass              0.681             46.9                           0.716                3.23             -0.310                                 ok            True                  False
  SOXL           83.33               12            9.81             18.32        258.95               249.48         0.671          pass              0.256             28.8                           0.617                6.38             -0.220                                 ok            True                  False
  UPRO           84.62               26            0.72              0.72        141.53                55.16         0.635          pass              0.462             56.2                           0.624               -2.09             -0.204                                 ok            True                  False
  ASML           91.67               12            3.39             47.21       1969.21                71.16         0.577          pass              0.493             37.0                           0.636                6.55              0.351                                 ok            True                  False
  INTC           90.00               20            4.03              3.94        137.94                95.61         0.521          pass              0.451             21.9                           0.360               14.48              0.919                                 ok            True                  False
  MPWR           87.88               33            0.60              5.77       1379.89                91.02         0.698          pass              0.686             84.3                           0.923               -8.32             -1.319            downtrend_blocked_slope           False                  False
  AVGO           78.95               19            1.79              4.72        375.73                74.76         0.686          pass              0.207             26.1                           0.361               -1.36             -0.599                                 ok           False                  False
  MCHP           92.00               25            1.22              0.78         90.87                74.43         0.664          pass              0.640             51.3                           0.555               -5.79             -0.969            downtrend_blocked_slope           False                  False
  QCOM           89.47               38            0.05              0.07        184.76                83.64         0.644          pass              0.797             97.7                           0.672              -13.72             -1.965 downtrend_blocked_slope_and_streak           False                  False
  NXPI           90.62               32            0.48              0.94        280.63                65.46         0.623          pass              0.756             87.9                           0.888               -7.35             -1.138            downtrend_blocked_slope           False                  False
   ADI           90.91               33            0.44              1.23        396.64                64.06         0.623          pass              0.751             81.6                           0.851               -4.95             -0.900            downtrend_blocked_slope           False                  False
   WDC           91.67               12            4.61             20.61        629.89               116.88         0.612          pass              0.506             40.0                           0.723              -10.54             -1.669            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-30T17:05:09.028498-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500                   entry {"allocated_cash": 14640.0, "asset_type": "option", "contract_symbol": "GILD260821C00130000", "contracts": 32, "early_entry_score": 0.533, "entry_mode": "regular", "entry_option_price": 4.575, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 807.0, "option_spread_pct": 7.65, "option_volume": 40.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.563}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
2026-06-29T14:50:09.505108-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-29", "training_samples": 5314, "window": 5}
2026-06-29T12:00:02.850105-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701095714)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701095714)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701095714)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701095714)

</details>
