# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=222ms, nekobox=215ms, status=no)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=215ms, nekobox=182ms, status=no)
3. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS`
4. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
6. `AKUN-004-DIGITALOCEAN-VLESS-WS-78MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS`
8. `AKUN-006-U1HOST-FRA-VLESS-WS-74MS`
9. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-76MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-009-1PASSWORD-VLESS-WS-107MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-85MS`
13. `AKUN-013-EU-VLESS-WS-94MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-68MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-117MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-MEDIUM-VLESS-WS-133MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-124MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-OPENAI-VLESS-WS-82MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-251MS` (url=577ms, status=HTTP 204)
20. `AKUN-020-MICROSOFT-VLESS-WS-265MS` (url=552ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-233MS` (url=506ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-301MS` (url=4259ms, status=HTTP 204)
23. `AKUN-024-US-VLESS-WS-97MS` (url=218ms, status=HTTP 204)
24. `AKUN-027-JISON-VLESS-WS-395MS` (url=602ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-466MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
