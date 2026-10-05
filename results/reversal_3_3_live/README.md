# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 09:55:04 EDT`
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

- Cash: `$88,586.80`
- Equity: `$88,586.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.87               31            2.64              3.03        162.41               114.85         0.683          pass              0.378             22.1                           0.298               12.37              0.928                      ok            True                  False
  AMGN           85.19               27            0.66              1.85        402.25                47.11         0.578          pass              0.477             56.0                           0.397                1.84              0.114                      ok            True                  False
  ASML           80.65               31            0.86             11.27       1862.48                42.39         0.540          pass              0.357             48.5                           0.434                8.17              0.833                      ok            True                  False
   TRI           85.19               27            1.54              1.05         97.17                53.36         0.535          pass              0.356             17.1                           0.329                0.72              0.051                      ok            True                  False
   ADI           86.36               22            1.31              3.83        415.51                32.86         0.521          pass              0.360             19.5                           0.270                7.49              0.780                      ok            True                  False
  TMUS           85.71               28            0.63              0.72        163.33                31.57         0.516          pass              0.434             36.8                           0.326               -1.61             -0.150                      ok            True                  False
   XEL           85.00               20            0.62              0.31         71.27                18.48         0.514          pass              0.343             30.5                           0.229               -1.25             -0.059                      ok            True                  False
  NXPI           84.00               25            1.50              2.56        242.56                37.68         0.502          pass              0.331             24.8                           0.206                3.27              0.332                      ok            True                  False
  MRVL           81.82               33            1.25              2.38        271.27                54.74         0.500          pass              0.325             24.3                           0.246                4.47              0.449                      ok            True                  False
  DRAM           80.56               36            0.27              0.12         61.69                54.09         0.576          pass              0.408             54.2                           0.413               -0.01             -0.121                      ok           False                  False
  AMAT           85.00               40            0.35              1.34        539.47                49.71         0.545          pass              0.598             69.9                           0.452               15.92              1.643                      ok           False                  False
  INTC           82.76               29            2.28              1.90        118.51                74.20         0.544          pass              0.412             52.4                           0.747               -4.25             -0.550 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                               detail
2026-10-05T09:55:04.847980-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "ZS261120C00200000", "fill_price": 17.525, "pnl": 7222.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.01, "ticker": "ZS"}
2026-10-05T03:00:05.114767-04:00   data_refresh  data_refresh                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00 share_ext_0255 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00 share_ext_0250 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00 share_ext_0245 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00 share_ext_0240 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00 share_ext_0235 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00 share_ext_0230 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:25:01.959731-04:00 share_ext_0225 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:20:06.968956-04:00 share_ext_0220 market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005095504)

</details>
