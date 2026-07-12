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
1. `AKUN-001-ZVC-VLESS-WS-69MS` (url=213ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=199ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=211ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, nekobox=225ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=217ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=200ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=232ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=212ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=207ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS` (url=228ms, nekobox=248ms, status=yes)
11. `AKUN-011-DIGITALOCEAN-VLESS-WS-84MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=199ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-91MS` (url=228ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=225ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-134MS` (url=203ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-142MS` (url=206ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-119MS` (url=228ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-90MS` (url=234ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-244MS` (url=521ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-236MS` (url=489ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-244MS` (url=499ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-247MS` (url=503ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-234MS` (url=496ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
