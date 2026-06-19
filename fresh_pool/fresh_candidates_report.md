# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=222ms, nekobox=227ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-77MS` (url=206ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=228ms, nekobox=233ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-108MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-144MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-129MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-266MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-272MS` (url=570ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-271MS` (url=511ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-274MS` (url=567ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-305MS` (url=3799ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-276MS` (url=560ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-321MS` (url=2383ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-389MS` (url=608ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-381MS` (url=560ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-383MS` (url=645ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-380MS` (url=604ms, status=HTTP 204)
22. `AKUN-034-UNKNOWN-VLESS-WS-552MS` (url=1401ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
