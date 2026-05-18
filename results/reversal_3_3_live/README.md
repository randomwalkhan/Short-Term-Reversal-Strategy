# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 10:27:37 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$16,120.00`
- Equity: `$30,595.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$-50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   1      5     14525.0                 14475.0        29.05          28.95       350.6        347.85          bid_ask_mid                      28.95                bid_ask_mid                    True           -50.0                  -0.34          97.3               37              0.63         45.67            51.5                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               34            0.70              0.53        108.54               115.99         0.706            pass              0.871             80.3                           0.377               12.77              0.774                                 ok            True                  False
  QCOM           87.50               16            2.16              3.04        200.19                99.06         0.678            pass              0.351             14.5                           0.267               17.08              1.157                                 ok            True                  False
  CSCO           88.89               18            1.33              1.10        117.74                49.84         0.621            pass              0.418             21.9                           0.251               25.92              2.709                                 ok            True                  False
  ASML           82.76               29            1.07             11.29       1496.97                50.55         0.528            pass              0.369             38.7                           0.420                7.18              0.565                                 ok            True                  False
  SNPS           97.14               35            0.82              2.87        501.19                42.05         0.519            pass              0.801             60.7                           0.537                0.16              0.046                                 ok            True                  False
   TXN           93.55               31            0.42              0.89        302.35                68.84         0.689            pass              0.766             65.1                           0.470                7.87              0.939                                 ok           False                  False
  INSM           66.67               27            1.84              1.41        108.54               111.34         0.653            pass              0.349             56.7                           0.662              -23.48             -2.237 downtrend_blocked_slope_and_streak           False                  False
  MCHP           87.80               41            0.44              0.29         93.73                53.01         0.510            pass              0.619             53.4                           0.319               -1.95             -0.527 downtrend_blocked_slope_and_streak           False                  False
  AVGO           91.67               24            1.67              4.98        423.06                43.18         0.493 below_threshold              0.544             30.2                           0.407                0.38              0.085                                 ok           False                  False
  AAPL           85.71               28            0.74              1.55        299.57                22.88         0.492 below_threshold              0.434             37.4                           0.416                7.75              0.723                                 ok           False                  False
  META           77.78               36            0.61              2.61        613.11                37.75         0.488 below_threshold              0.449             75.7                           0.722                0.01              0.070                                 ok           False                  False
  AMGN           83.33               24            0.68              1.54        325.65                26.25         0.487 below_threshold              0.401             56.8                           0.503                0.83              0.123                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                      detail
2026-05-18T10:27:37.648386-04:00 early_entry_1025 entry_skipped                  {"reason": "no_candidate"}
2026-05-18T03:00:02.728743-04:00     data_refresh  data_refresh                               {'saved': 92}
2026-05-16T02:55:09.369538-04:00   share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:50:03.948678-04:00   share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:45:01.564452-04:00   share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:40:01.759045-04:00   share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:35:01.904686-04:00   share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:30:04.868117-04:00   share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:25:04.937005-04:00   share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:20:05.919345-04:00   share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518102737)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518102737)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518102737)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518102737)

</details>
