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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-SPEEDTEST-VLESS-WS-109MS` (url=265ms, nekobox=212ms, status=no)
2. `AKUN-001-CHATGPT-VLESS-WS-102MS`
3. `AKUN-003-SPEEDTEST-VLESS-WS-119MS` (url=273ms, nekobox=206ms, status=no)
4. `AKUN-002-UNKNOWN-VLESS-WS-129MS`
5. `AKUN-003-ZVC-VLESS-WS-116MS`
6. `AKUN-004-UNKNOWN-VLESS-WS-124MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-110MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-126MS`
10. `AKUN-010-SPEEDTEST-VLESS-WS-116MS` (url=256ms, nekobox=190ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-155MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-151MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-159MS` (url=297ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-97MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-174MS` (url=336ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-156MS` (url=379ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-169MS` (url=335ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-159MS` (url=273ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-225MS` (url=311ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=295ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-285MS` (url=745ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-605MS` (url=745ms, status=HTTP 204)
24. `AKUN-030-AS210546-IPV4-VLESS-WS-639MS` (url=862ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-579MS` (url=1061ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
