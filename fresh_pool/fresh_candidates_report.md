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
1. `AKUN-001-UNKNOWN-VLESS-WS-85MS` (url=353ms, nekobox=370ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-101MS` (url=327ms, nekobox=7171ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-94MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-105MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-120MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-98MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-105MS` (url=362ms, nekobox=210ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-126MS`
13. `AKUN-013-466688-VLESS-WS-120MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-132MS` (url=398ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-144MS` (url=483ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-142MS` (url=362ms, status=HTTP 204)
17. `AKUN-017-ORG-VLESS-WS-148MS` (url=336ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-131MS` (url=340ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-150MS` (url=361ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=301ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-108MS` (url=341ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-146MS` (url=312ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-205MS` (url=392ms, status=HTTP 204)
24. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-208MS` (url=448ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-116MS` (url=431ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
