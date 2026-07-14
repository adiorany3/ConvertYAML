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
1. `AKUN-001-UNKNOWN-VLESS-WS-101MS` (url=315ms, nekobox=314ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=357ms, nekobox=306ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=275ms, nekobox=316ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-89MS` (url=327ms, nekobox=367ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-106MS` (url=291ms, nekobox=374ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-117MS` (url=466ms, nekobox=353ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-115MS` (url=304ms, nekobox=337ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=309ms, nekobox=340ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS` (url=323ms, nekobox=337ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-123MS` (url=377ms, nekobox=344ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-128MS` (url=289ms, status=HTTP 204)
12. `AKUN-012-PAGES-VLESS-WS-128MS` (url=404ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-126MS` (url=347ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-92MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-121MS` (url=375ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-127MS` (url=322ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-167MS` (url=371ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-163MS` (url=377ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-170MS` (url=327ms, status=HTTP 204)
20. `AKUN-020-VOV-VLESS-WS-182MS` (url=427ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=355ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-135MS` (url=377ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-303MS` (url=600ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-312MS` (url=599ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-308MS` (url=662ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
