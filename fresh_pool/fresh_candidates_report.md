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
1. `AKUN-001-ALIBABA-VLESS-WS-113MS` (url=303ms, nekobox=318ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=267ms, nekobox=309ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-132MS` (url=251ms, nekobox=337ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS` (url=282ms, nekobox=466ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-123MS` (url=336ms, nekobox=299ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS` (url=295ms, nekobox=296ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-142MS` (url=292ms, nekobox=299ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-130MS` (url=282ms, nekobox=303ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-133MS` (url=311ms, nekobox=307ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=322ms, nekobox=310ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-151MS` (url=308ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-124MS` (url=299ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=290ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-155MS` (url=297ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-143MS` (url=274ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=296ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-163MS` (url=274ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-119MS` (url=290ms, status=HTTP 204)
19. `AKUN-019-VULTR-VLESS-WS-167MS` (url=290ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-190MS` (url=308ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-136MS` (url=302ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-323MS` (url=735ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-297MS` (url=5193ms, status=HTTP 204)
24. `AKUN-024-PUBLICDOMAINREGISTRY-NET-VLESS-WS-328MS` (url=791ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-330MS` (url=723ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
