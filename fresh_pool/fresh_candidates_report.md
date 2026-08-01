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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=220ms, nekobox=171ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-56MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS`
4. `AKUN-003-ZVC-VLESS-WS-70MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS`
11. `AKUN-010-EE-WELCOMEHOST-20190515-VLESS-WS-133MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-87MS` (url=201ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-101MS` (url=201ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-160MS` (url=216ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-112MS` (url=221ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-87MS` (url=202ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-251MS` (url=491ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-241MS` (url=490ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-397MS` (url=730ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-391MS` (url=649ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-387MS` (url=664ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-434MS` (url=1294ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-475MS` (url=1293ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-483MS` (url=1181ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
