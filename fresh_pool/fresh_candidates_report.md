# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-DEV-VLESS-WS-113MS` (url=314ms, nekobox=336ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-131MS` (url=325ms, nekobox=413ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-120MS` (url=368ms, nekobox=636ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-96MS` (url=307ms, nekobox=359ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-152MS` (url=387ms, nekobox=460ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-110MS` (url=370ms, nekobox=326ms, status=yes)
7. `AKUN-007-SPEEDTEST-VLESS-WS-182MS` (url=338ms, nekobox=256ms, status=no)
8. `AKUN-007-WEBEX-VLESS-WS-121MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-180MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-167MS` (url=512ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-122MS` (url=515ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-258MS` (url=587ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-328MS` (url=808ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-342MS` (url=4816ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-366MS` (url=702ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-106MS` (url=385ms, status=HTTP 204)
19. `AKUN-020-SPEEDTEST-VLESS-WS-99MS` (url=665ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-135MS` (url=305ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-99MS` (url=831ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-592MS` (url=961ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-648MS` (url=1151ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
