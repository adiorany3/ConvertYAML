# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=288ms, nekobox=229ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS` (url=208ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=224ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS` (url=205ms, nekobox=228ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=255ms, nekobox=224ms, status=yes)
6. `AKUN-006-BROADNNET-KR-VLESS-WS-82MS` (url=194ms, nekobox=259ms, status=yes)
7. `AKUN-007-KIRINO-31-25-88-0-24-VLESS-WS-93MS` (url=195ms, nekobox=223ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-61MS` (url=208ms, nekobox=240ms, status=yes)
9. `AKUN-009-DIGITALOCEAN-VLESS-WS-116MS` (url=223ms, nekobox=209ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-367MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-372MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-433MS` (url=824ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-361MS` (url=743ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-415MS` (url=814ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-361MS` (url=756ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-408MS` (url=870ms, status=HTTP 204)
17. `AKUN-021-UNKNOWN-VLESS-WS-730MS` (url=1089ms, status=HTTP 204)
18. `AKUN-024-UNKNOWN-VLESS-WS-786MS` (url=3702ms, status=HTTP 204)
19. `AKUN-031-DEV-VLESS-WS-250MS` (url=546ms, status=HTTP 204)
20. `AKUN-032-UNKNOWN-VLESS-WS-851MS` (url=1895ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
