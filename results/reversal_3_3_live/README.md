# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 02:55:06 EST`
Last processed slot: `share_ext_0255`

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

- Cash: `$52,781.30`
- Equity: `$105,756.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$4,810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 52975.0        37.05          40.75      380.27        372.27     last_price_stale                        NaN                unavailable                   False          4810.0                   9.99         94.74               19              2.72          61.7             0.2                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et         slot   event_type                    detail
2026-11-20T01:25:03.363046-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:15:06.809821-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:10:05.934124-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:05:05.898904-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T01:00:05.809710-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:55:04.836951-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:50:02.820195-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:45:05.761865-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
2026-11-20T00:40:04.740309-05:00 data_refresh data_refresh {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120025506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120025506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120025506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120025506)

</details>
