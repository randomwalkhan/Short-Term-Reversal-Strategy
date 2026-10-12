# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:15:06 EDT`
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

- Cash: `$58,874.30`
- Equity: `$119,674.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$2,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 60800.0         3.65            3.8       59.31         60.13          bid_ask_mid                        3.8                bid_ask_mid                    True          2400.0                   4.11          93.1               29              1.17         50.42            52.0                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           83.33               36            0.67              2.38        508.97                55.08         0.570            pass              0.456             45.7                           0.376               21.31              2.067                                 ok            True                  False
    ZS           92.59               27            2.04              3.34        232.30                75.53         0.533            pass              0.548             15.1                           0.197               14.83              1.653                                 ok            True                  False
  ABNB           86.67               30            1.03              1.20        165.36                38.25         0.511            pass              0.483             40.4                           0.292                5.18              0.464                                 ok            True                  False
  QCOM           86.96               23            1.36              1.67        174.78                55.68         0.600            pass              0.418             28.6                           0.254               -7.66             -0.727 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               30            1.99             10.89        778.33                69.65         0.552            pass              0.392             38.3                           0.474              -16.72             -2.202            downtrend_blocked_slope           False                  False
   WDC           80.00               35            1.21              3.36        395.84                64.73         0.541            pass              0.388             55.7                           0.686              -13.40             -1.779            downtrend_blocked_slope           False                  False
  INTC           81.82               22            2.62              1.92        103.88                69.66         0.535            pass              0.246             21.3                           0.237              -12.13             -1.435 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           89.47               19            0.27              0.04         20.64                20.79         0.528            pass              0.562             65.6                           0.507               -3.97             -0.355            downtrend_blocked_slope           False                  False
  CSCO           50.00                4            2.48              2.06        117.51                33.46         0.518            pass              0.095             14.5                           0.202                8.58              1.138                                 ok           False                  False
  TEAM          100.00               43            0.01              0.02        206.78                49.66         0.514            pass              0.936             95.0                           0.437               15.81              1.685                                 ok           False                  False
  DASH           76.92               13            2.71              3.72        194.90                43.05         0.505            pass              0.149             26.1                           0.268                7.17              0.721                                 ok           False                  False
  PAYX           81.82               44            0.16              0.12        103.93                39.82         0.499 below_threshold              0.392             31.2                           0.162                4.55              0.561                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                             {'saved': 90, 'empty': 3}
2026-10-10T02:55:05.468213-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:50:06.073538-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:45:04.438965-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:40:05.495022-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-10T02:35:05.586025-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012101506)

</details>
