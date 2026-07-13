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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-101MS` (url=399ms, nekobox=367ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-107MS` (url=350ms, nekobox=393ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS` (url=315ms, nekobox=337ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-118MS` (url=366ms, nekobox=408ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS` (url=259ms, nekobox=7175ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-120MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-120MS`
8. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-116MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-131MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=374ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-135MS` (url=323ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-107MS` (url=346ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-122MS` (url=297ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-114MS` (url=317ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-133MS` (url=351ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-129MS` (url=358ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-120MS` (url=349ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=354ms, status=HTTP 204)
21. `AKUN-022-PUBLICDOMAINREGISTRY-NET-VLESS-WS-151MS` (url=365ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-208MS` (url=476ms, status=HTTP 204)
23. `AKUN-025-OVH-VLESS-WS-133MS` (url=347ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-304MS` (url=659ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-329MS` (url=710ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
