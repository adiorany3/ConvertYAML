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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=219ms, nekobox=284ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-96MS` (url=219ms, nekobox=236ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=235ms, nekobox=240ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-113MS` (url=225ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=252ms, nekobox=269ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-114MS` (url=219ms, nekobox=268ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS` (url=213ms, nekobox=245ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-115MS` (url=240ms, nekobox=263ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=206ms, nekobox=235ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-114MS` (url=208ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=285ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-367MS` (url=636ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-360MS` (url=755ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-412MS` (url=865ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-415MS` (url=898ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-389MS` (url=842ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-420MS` (url=746ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-387MS` (url=744ms, status=HTTP 204)
21. `AKUN-031-CLOUDFLARE-VLESS-WS-641MS` (url=1382ms, status=HTTP 204)
22. `AKUN-033-UNKNOWN-VLESS-WS-798MS` (url=2694ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
