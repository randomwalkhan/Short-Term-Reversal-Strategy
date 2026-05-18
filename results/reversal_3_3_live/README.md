# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:15:03 EDT`
Last processed slot: `early_entry_1115`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$2,570.00`
- Equity: `$29,070.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$-1,575.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13400.0        13.55           13.4      241.03        241.65          bid_ask_mid                       13.4                bid_ask_mid                    True          -150.0                  -1.11         97.62               42              0.58         61.06           59.51                  33.53                3069.0           22.0               0.11                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-15                   1      5     14525.0                 13100.0        29.05           26.2      350.60        343.33          bid_ask_mid                       26.2                bid_ask_mid                    True         -1425.0                  -9.81         97.30               37              0.63         45.67           50.01                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.10               29            0.62              1.31        302.17                68.84         0.688            pass              0.702             52.4                           0.478                7.65              0.930                                 ok            True                  False
  CSCO           91.30               23            1.17              0.97        117.80                49.84         0.601            pass              0.558             36.7                           0.393               26.13              2.716                                 ok            True                  False
  AMGN           92.31               13            1.03              2.34        325.31                26.25         0.551            pass              0.506             34.4                           0.302                0.48              0.107                                 ok            True                  False
  SNPS           95.65               23            1.88              6.62        499.58                42.05         0.522            pass              0.600             20.2                           0.270               -0.91             -0.003                                 ok            True                  False
  AAPL           90.00               20            1.19              2.51        299.16                22.88         0.521            pass              0.401              5.3                           0.251                7.26              0.702                                 ok            True                  False
  INTC          100.00               34            0.46              0.35        108.62               115.99         0.719            pass              0.893             87.2                           0.700               13.05              0.785                                 ok           False                  False
  QCOM           87.50                8            2.76              3.89        199.82                99.06         0.677            pass              0.357             29.7                           0.468               16.36              1.129                                 ok           False                  False
  INSM           65.22               23            2.53              1.93        108.31               111.34         0.633            pass              0.271             40.5                           0.299              -24.02             -2.269 downtrend_blocked_slope_and_streak           False                  False
  MCHP           84.85               33            0.76              0.50         93.64                53.01         0.533            pass              0.473             45.7                           0.440               -2.27             -0.542 downtrend_blocked_slope_and_streak           False                  False
  META           74.07               27            0.95              4.09        612.48                37.75         0.519            pass              0.351             62.0                           0.550               -0.33              0.054                                 ok           False                  False
  AVGO           92.59               27            1.30              3.86        423.53                43.18         0.499 below_threshold              0.636             45.8                           0.648                0.76              0.102                                 ok           False                  False
  MSFT           84.00               25            0.96              2.82        420.71                29.78         0.499 below_threshold              0.426             56.4                           0.289                1.03              0.024                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-18T11:15:03.521300-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:10:02.609364-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:05:05.558676-04:00 early_entry_1105         entry {"allocated_cash": 13550.0, "asset_type": "option", "contract_symbol": "TTWO260618C00250000", "contracts": 10, "early_entry_score": 0.906, "entry_mode": "early", "entry_option_price": 13.55, "execution_mode": "option", "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3069.0, "option_spread_pct": 11.07, "option_volume": 22.0, "success_rate": 97.62, "ticker": "TTWO", "timing_score": 0.402}
2026-05-18T11:00:09.683441-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T10:27:37.648386-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T03:00:02.728743-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-16T02:55:09.369538-04:00   share_ext_0255 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:50:03.948678-04:00   share_ext_0250 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:45:01.564452-04:00   share_ext_0245 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:40:01.759045-04:00   share_ext_0240 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518111503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518111503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518111503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518111503)

</details>
