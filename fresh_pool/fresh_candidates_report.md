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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=235ms, nekobox=257ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-79MS` (url=212ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=211ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=223ms, nekobox=187ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-124MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-130MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-123MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=279ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-132MS` (url=239ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-128MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-129MS` (url=268ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-95MS` (url=289ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-160MS` (url=279ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-113MS` (url=250ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-115MS` (url=266ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-107MS` (url=249ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
