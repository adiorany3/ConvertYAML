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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=228ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=212ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=228ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=213ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS` (url=219ms, nekobox=229ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=217ms, nekobox=255ms, status=yes)
9. `AKUN-009-PUBLICDOMAINREGISTRY-NET-VLESS-WS-99MS` (url=229ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=210ms, nekobox=232ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-86MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-UDACITY-VLESS-WS-122MS` (url=246ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-77MS` (url=232ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-135MS` (url=204ms, status=HTTP 204)
16. `AKUN-017-POLICE-VLESS-WS-134MS` (url=247ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-143MS` (url=220ms, status=HTTP 204)
18. `AKUN-019-HETZNER-VLESS-WS-168MS` (url=233ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-164MS` (url=204ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-154MS` (url=235ms, status=HTTP 204)
21. `AKUN-022-466688-VLESS-WS-152MS` (url=230ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-245MS` (url=507ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-250MS` (url=498ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-249MS` (url=1867ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-271MS` (url=549ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
