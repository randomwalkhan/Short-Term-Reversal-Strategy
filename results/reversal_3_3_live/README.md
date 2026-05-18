# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:05:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$29,520.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$-1,125.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13550.0        13.55          13.55      241.03        241.03          bid_ask_mid                      13.55                bid_ask_mid                    True             0.0                   0.00         97.62               42              0.58         61.06           61.06                  33.53                3069.0           22.0               0.11                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-15                   1      5     14525.0                 13400.0        29.05          26.80      350.60        343.29          bid_ask_mid                      26.80                bid_ask_mid                    True         -1125.0                  -7.75         97.30               37              0.63         45.67           53.18                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           88.24               17            1.43              1.18        117.70                49.84         0.619          pass              0.395             22.4                           0.338               25.79              2.704                                 ok            True                  False
  AMGN           91.67               12            1.07              2.44        325.27                26.25         0.554          pass              0.475             31.8                           0.358                0.44              0.105                                 ok            True                  False
  SNPS           94.44               18            2.14              7.54        499.19                42.05         0.537          pass              0.520              9.1                           0.182               -1.18             -0.015                                 ok            True                  False
  AAPL           90.00               20            1.16              2.44        299.18                22.88         0.523          pass              0.399              4.6                           0.292                7.29              0.703                                 ok            True                  False
  ASML           81.48               27            1.49             15.63       1495.11                50.55         0.508          pass              0.299             32.0                           0.414                6.73              0.546                                 ok            True                  False
  INTC          100.00               38            0.22              0.17        108.70               115.99         0.710          pass              0.939             93.8                           0.659               13.31              0.795                                 ok           False                  False
   TXN           93.75               32            0.38              0.81        302.38                68.84         0.685          pass              0.794             70.7                           0.586                7.91              0.941                                 ok           False                  False
  QCOM           88.89                9            2.62              3.69        199.91                99.06         0.681          pass              0.405             33.3                           0.384               16.53              1.136                                 ok           False                  False
  INSM           66.67               24            2.35              1.79        108.37               111.34         0.640          pass              0.292             44.8                           0.474              -23.88             -2.261 downtrend_blocked_slope_and_streak           False                  False
  SHOP           86.05               43            0.23              0.16        100.21                79.48         0.607          pass              0.683             86.9                           0.370              -21.56             -1.956 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.97               33            0.16              0.12        106.76                32.79         0.528          pass              0.878             90.8                           0.427                2.19              0.227                                 ok           False                  False
  META           73.91               23            1.25              5.38        611.92                37.75         0.525          pass              0.289             50.0                           0.386               -0.63              0.040                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-18T11:05:05.558676-04:00 early_entry_1105         entry {"allocated_cash": 13550.0, "asset_type": "option", "contract_symbol": "TTWO260618C00250000", "contracts": 10, "early_entry_score": 0.906, "entry_mode": "early", "entry_option_price": 13.55, "execution_mode": "option", "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3069.0, "option_spread_pct": 11.07, "option_volume": 22.0, "success_rate": 97.62, "ticker": "TTWO", "timing_score": 0.402}
2026-05-18T11:00:09.683441-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T10:27:37.648386-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-18T03:00:02.728743-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92}
2026-05-16T02:55:09.369538-04:00   share_ext_0255 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:50:03.948678-04:00   share_ext_0250 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:45:01.564452-04:00   share_ext_0245 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:40:01.759045-04:00   share_ext_0240 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:35:01.904686-04:00   share_ext_0235 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-05-16T02:30:04.868117-04:00   share_ext_0230 market_closed                                                                                                                                                                                                                                                                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518110505)

</details>
