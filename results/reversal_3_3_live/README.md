# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-02 10:00:05 EST`
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

- Cash: `$58,976.55`
- Equity: `$123,176.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$6,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   1     30     58200.0                 64200.0         19.4           21.4      259.39        266.39          bid_ask_mid                       21.4                bid_ask_mid                    True          6000.0                  10.31          84.0               25              1.96         51.59           52.95                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-11-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL           81.82               11            1.20              0.67         79.53                18.77         0.529            pass              0.297             62.9                           0.691                4.95              0.406                                 ok            True                  False
   AEP           86.96               23            0.72              0.66        129.93                19.46         0.511            pass              0.379             18.6                           0.198                3.65              0.259                                 ok            True                  False
  INTC           71.43               28            2.24              1.03         65.32               126.81         0.764            pass              0.282             28.4                           0.295              -30.15             -2.596            downtrend_blocked_slope           False                  False
  FTNT           75.00                4            4.19              3.99        134.37                91.18         0.631            pass              0.067              1.5                           0.112              -23.98             -2.650 downtrend_blocked_slope_and_streak           False                  False
  ALNY           57.14                7            3.96              4.57        163.04               108.44         0.625            pass              0.118             18.4                           0.150              -32.07             -3.627            downtrend_blocked_slope           False                  False
  CTSH           91.18               34            0.73              0.33         64.97                51.72         0.555            pass              0.644             43.5                           0.381               -3.23             -0.856            downtrend_blocked_slope           False                  False
  TEAM          100.00               22            1.91              2.57        190.62                55.13         0.541            pass              0.577             14.3                           0.133              -12.43             -1.452            downtrend_blocked_slope           False                  False
    MU           76.47               34            0.95              5.89        882.21                60.34         0.536            pass              0.333             39.7                           0.274               -3.16              0.171                                 ok           False                  False
  CSCO           77.27               22            1.02              0.75        104.19                35.63         0.524            pass              0.225             31.0                           0.245               -2.87             -0.043           downtrend_blocked_streak           False                  False
   KDP           96.77               31            0.15              0.04         35.82                21.81         0.510            pass              0.851             86.6                           0.670                3.85              0.353                                 ok           False                  False
  AAPL           93.33               15            1.26              3.05        343.32                14.54         0.497 below_threshold              0.478             13.2                           0.171               -0.78              0.033                                 ok           False                  False
    ZS           84.62               13            3.36              5.59        235.43                62.20         0.495 below_threshold              0.230             12.4                           0.142                8.15              1.070                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-02T10:00:05.841210-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T03:00:04.577568-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-31T02:55:06.398168-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:50:05.964599-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:45:05.451859-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:40:06.038699-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:35:06.236503-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:30:05.652864-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:25:01.174270-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-31T02:20:06.862130-04:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261102100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261102100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261102100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261102100005)

</details>
