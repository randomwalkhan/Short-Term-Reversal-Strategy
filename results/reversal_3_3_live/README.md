# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-24 02:05:06 EDT`
Last processed slot: `share_ext_0205`

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

- Cash: `$1,161.80`
- Equity: `$154,001.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$9,170.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   0    657     72270.0                 78840.0         1.10            1.2       44.42         44.43          bid_ask_mid                        1.2                bid_ask_mid                    True          6570.0                   9.09          80.0               15              0.97         20.09           23.17                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 74000.0        17.85           18.5      223.97        227.83          bid_ask_mid                       18.5                bid_ask_mid                    True          2600.0                   3.64         100.0               38              0.68         80.16           77.96                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-24)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-24T02:05:06.262281-04:00 share_ext_0205 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:00:04.364633-04:00 share_ext_0200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:55:05.308325-04:00 share_ext_0155 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:50:02.284653-04:00 share_ext_0150 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:45:04.134613-04:00 share_ext_0145 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:40:06.128943-04:00 share_ext_0140 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:35:06.258035-04:00 share_ext_0135 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:30:05.937395-04:00 share_ext_0130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:25:04.232813-04:00 share_ext_0125 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T01:20:04.212135-04:00 share_ext_0120 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261024020506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261024020506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261024020506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261024020506)

</details>
